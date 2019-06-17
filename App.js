/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow
 */

import React, {Component} from 'react';
import {Platform, StyleSheet, Text, View} from 'react-native';


export default class App extends Component {
  render() {
    return (
      <View style={styles.container}>
        <View style={styles.innerContainer}></View>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#c2383b',
  },
  innerContainer: {
    flex: 1,
    alignItems: 'center',
    backgroundColor: '#c2383b',
    borderWidth: 5,
    borderColor: '#e3d342',
    margin: 10,
  },

});

